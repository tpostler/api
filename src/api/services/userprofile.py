from _main_.utils.massenergize_errors import MassEnergizeAPIError
from _main_.utils.massenergize_response import MassenergizeResponse
from _main_.utils.common import serialize, serialize_all
from api.store.userprofile import UserStore
from _main_.utils.context import Context

from _main_.utils.emailer.send_email import send_massenergize_email
from _main_.utils.emailer.send_email import send_massenergize_rich_email

from _main_.utils.constants import COMMUNITY_URL_ROOT

class UserService:
  """
  Service Layer for all the users
  """

  def __init__(self):
    self.store =  UserStore()

  def get_user_info(self, context: Context, args) -> (dict, MassEnergizeAPIError):
    user, err = self.store.get_user_info(context, args)
    if err:
      return None, err
    return serialize(user, full=True), None

  def add_household(self,context: Context, args) -> (dict, MassEnergizeAPIError):
    household, err = self.store.add_household(context, args)
    if err:
      return None, err
    return serialize(household, full=True), None

  def remove_household(self,context: Context, args) -> (dict, MassEnergizeAPIError):
    household, err = self.store.remove_household(context, args)
    if err:
      return None, err
    return household, None

  def list_users(self, community_id) -> (list, MassEnergizeAPIError):
    user, err = self.store.list_users(community_id)
    if err:
      return None, err
    return serialize_all(user), None


  def list_actions_todo(self, context: Context, args) -> (list, MassEnergizeAPIError):
    actions_todo, err = self.store.list_todo_actions(context, args)
    if err:
      return None, err
    return serialize_all(actions_todo), None

  def list_actions_completed(self, context: Context, args) -> (list, MassEnergizeAPIError):
    actions_completed, err = self.store.list_completed_actions(context, args)
    if err:
      return None, err
    return serialize_all(actions_completed), None

  def list_events_for_user(self, context: Context, args) -> (list, MassEnergizeAPIError):
    events, err = self.store.list_events_for_user(context, args)
    if err:
      return None, err
    return serialize_all(events), None


  def create_user(self, context: Context, args) -> (dict, MassEnergizeAPIError):
    user, err = self.store.create_user(context, args)
    if err:
      return None, err
    #send email here import the create user email function and hopefully that works

    subject = 'Welcome to the MassEnergize Movement'
    community = 'your community'
    homelink = COMMUNITY_URL_ROOT
    logo = 'https://s3.us-east-2.amazonaws.com/community.massenergize.org/static/media/logo.ee45265d.png'
    actionslink = homelink
    eventslink = homelink
    serviceslink = homelink
    privacylink = homelink
    if len(user.communities.all()) > 0: 
      community = user.communities.all()[0]
      subject = 'Welcome to %s' %(community)
      homelink = '%s/%s' %(COMMUNITY_URL_ROOT, community)
      l = community.logo
      if l and l.file:
        logo = l.file.url
      actionslink = '%s/actions' %(homelink)
      eventslink = '%s/events' %(homelink)
      serviceslink = '%s/services' %(homelink)
      privacylink = "{0}/policies?name=Privacy%20Policy".format(homelink)
    
    content_variables = {
      'name': user.preferred_name,
      'community': community,
      'homelink':homelink,
      'logo':logo,
      'actionslink':actionslink,
      'eventslink':eventslink,
      'serviceslink':serviceslink,
      'privacylink':privacylink
      }
    send_massenergize_rich_email(subject, user.email, 'user_registration_email.html', content_variables)

    return serialize(user), None


  def update_user(self, args) -> (dict, MassEnergizeAPIError):
    user, err = self.store.update_user(args)
    if err:
      return None, err
    return serialize(user), None

  def delete_user(self, args) -> (dict, MassEnergizeAPIError):
    user, err = self.store.delete_user(args)
    if err:
      return None, err
    return serialize(user), None


  def list_users_for_community_admin(self, context, community_id) -> (list, MassEnergizeAPIError):
    users, err = self.store.list_users_for_community_admin(context, community_id)
    if err:
      return None, err
    return serialize_all(users), None


  def list_users_for_super_admin(self, context) -> (list, MassEnergizeAPIError):
    users, err = self.store.list_users_for_super_admin(context)
    if err:
      return None, err
    return serialize_all(users), None


  def add_action_todo(self, context, args) -> (dict, MassEnergizeAPIError):
    user, err = self.store.add_action_todo(context, args)
    if err:
      return None, err
    return serialize(user, full=True), None

  def add_action_completed(self, context, args) -> (dict, MassEnergizeAPIError):
    user, err = self.store.add_action_completed(context, args)
    if err:
      return None, err
    return serialize(user, full=True), None