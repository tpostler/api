from database.models import Subscriber, UserProfile, Community
from _main_.utils.massenergize_errors import MassEnergizeAPIError, InvalidResourceError, ServerError, CustomMassenergizeError
from _main_.utils.massenergize_response import MassenergizeResponse
from _main_.utils.context import Context
from django.db.models import Q

class SubscriberStore:
  def __init__(self):
    self.name = "Subscriber Store/DB"

  def get_subscriber_info(self, subscriber_id) -> (dict, MassEnergizeAPIError):
    try:
      subscriber = Subscriber.objects.get(id=subscriber_id)
      if not subscriber:
        return None, InvalidResourceError()
      return subscriber, None
    except Exception as e:
      return None, CustomMassenergizeError(e)

  def list_subscribers(self, community_id) -> (list, MassEnergizeAPIError):
    subscribers = Subscriber.objects.filter(community__id=community_id)
    if not subscribers:
      return [], None
    return subscribers, None


  def create_subscriber(self, community_id, args) -> (dict, MassEnergizeAPIError):
    try:
      new_subscriber = Subscriber.objects.create(**args)
      new_subscriber.save()
      if community_id:
        community = Community.objects.get(id=community_id)
        new_subscriber.community = community

        #community.subscribers.add(new_subscriber)
        #community.save()
      return new_subscriber, None
    except Exception as e:
      return None, CustomMassenergizeError(e)


  def update_subscriber(self, subscriber_id, args) -> (dict, MassEnergizeAPIError):
    try:
      community_id = args.pop("community_id", None)
      subscriber = Subscriber.objects.filter(id=subscriber_id)
      if not subscriber:
        return None, InvalidResourceError()

      subscriber.update(**args)
      subscriber: Subscriber = subscriber.first()
      if subscriber and community_id:
        community: Community = Community.objects.filter(pk=community_id).first()
        if community:
          community.subscribers.add(subscriber)
          community.save()
      return subscriber, None
    except Exception as e:
      return None, CustomMassenergizeError(str(e))


  def delete_subscriber(self, subscriber_id) -> (Subscriber, MassEnergizeAPIError):
    try:
      #find the subscriber
      subscribers_to_delete = Subscriber.objects.filter(id=subscriber_id)
      subscribers_to_delete.update(is_deleted=True)
      if not subscribers_to_delete:
        return None, InvalidResourceError()
      return subscribers_to_delete.first(), None
    except Exception as e:
      return None, CustomMassenergizeError(str(e))

  def copy_subscriber(self, subscriber_id) -> (Subscriber, MassEnergizeAPIError):
    try:
      #find the subscriber
      subscriber_to_copy = Subscriber.objects.filter(id=subscriber_id).first()
      if not subscriber_to_copy:
        return None, InvalidResourceError()
      
      new_subscriber = subscriber_to_copy
      new_subscriber.pk = None
      new_subscriber.name = subscriber_to_copy.name + ' Copy'
      new_subscriber.save()
      return new_subscriber, None
    except Exception as e:
      print(e)
      return None, CustomMassenergizeError(str(e))


  def list_subscribers_for_community_admin(self, context: Context, community_id) -> (list, MassEnergizeAPIError):
    try:
      if context.user_is_super_admin:
        return self.list_subscribers_for_super_admin(context)

      elif not context.user_is_community_admin:
        return None, CustomMassenergizeError("Sign in as a valid community admin")

      if not community_id:
        user = UserProfile.objects.get(pk=context.user_id)
        admin_groups = user.communityadmingroup_set.all()
        communities = [ag.community for ag in admin_groups]
        subscribers = None
        for ag in admin_groups:
          if not subscribers:
            subscribers = ag.community.subscriber_set.all().filter(is_deleted=False)
          else:
            subscribers |= ag.community.subscriber_set.all().filter(is_deleted=False)

        return subscribers, None

      community: Community = Community.objects.get(pk=community_id)
      subscribers = community.subscriber_set.all().filter(is_deleted=False)
      return subscribers, None
 
    except Exception as e:
      print(e)
      return None, CustomMassenergizeError(e)


  def list_subscribers_for_super_admin(self, context: Context):
    try:
      subscribers = Subscriber.objects.filter(is_deleted=False)
      return subscribers, None
    except Exception as e:
      return None, CustomMassenergizeError(str(e))