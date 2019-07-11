"""
This file contains code to read data from the database.
"""
from  database.models import *
from database.utils.common import json_loader, retrieve_object, retrieve_all_objects

IS_PROD = True

def fetch_from_db(model, filter_args={}, 
  prefetch_related_args=[], select_related_args=[]):
  return (model.objects
    .select_related(*select_related_args)
    .filter(**filter_args)
    .prefetch_related(*prefetch_related_args))

def fetch_one_from_db(model, filter_args={}, 
  prefetch_related_args=[], select_related_args=[]):
  data = fetch_from_db(model, filter_args, 
    prefetch_related_args, select_related_args)
  if data:
    return data.first()
  return None 


def community_portal_home_page_data():
  """
  This function pulls and returns all data required for the community 
  portal home page and returns a json of this information
  """
  return json_loader('./database/raw_data/portal/homePageData.json')

def community_portal_user_data():
  """
  Returns the user data for the communty portal 
  """
  return json_loader('./database/raw_data/portal/user.json')

def community_portal_impact_data():
  """
  This function pulls and returns all impact data
  and returns a json of this information
  """
  return json_loader('./database/raw_data/portal/impactData.json')

def community_portal_website_menu():
  """
  Returns the menu for communty portal 
  """
  return json_loader('./database/raw_data/portal/menu.json')


def community_portal_actions_page_data(community_id='default'):
  """
  Returns all the possible actions for a community actions 
  """
  return json_loader('./database/raw_data/portal/actionsPageData.json')

def community_portal_events_page_data(community_id='default'):
  """
  Returns all the events for a community 
  """
  return json_loader('./database/raw_data/portal/eventsPageData.json')

def community_portal_about_us_page_data():
  """
  This function pulls and returns all data required for the community 
  portal about us page and returns a json of this information
  """
  return json_loader('./database/raw_data/portal/aboutUsData.json')

def community_portal_stories_page_data():
  """
  This function pulls and returns all data required for the community 
  portal stories page and returns a json of this information
  """
  return json_loader('./database/raw_data/portal/storiesPageData.json')


def super_admin_sidebar():
  return Menu.objects.filter(name="SuperAdmin-MainSideBar").first()

def super_admin_navbar():
  return Menu.objects.filter(name="SuperAdmin-MainNavBar").first()

def get_states_in_the_US():
  return json_loader('./database/raw_data/other/states.json')


def actions(args):
  filter_args = {}
  if "community_id" in args:
    filter_args["community"] = args["community_id"]
  if "action_id" in args:
    filter_args["id"] = args["action_id"]
  if "is_global" in args:
    filter_args["is_global"] = args["is_global"]
  actions =  fetch_from_db(Action, filter_args, ['tags'], ['community'])
  return actions


def events(args):
  filter_args = {}
  if "community_id" in args:
    filter_args["community"] = args["community_id"]
  if "event_id" in args:
    filter_args["id"] = args["action_id"]
  if "is_global" in args:
    filter_args["is_global"] = args["is_global"]
  events =  fetch_from_db(Event, filter_args, ['tags'], ['community'])
  return events



def communities(args):
  filter_args = {}
  if "community_id" in args:
    filter_args["community"] = args["community_id"]
  communities =  fetch_from_db(Community, filter_args)
  return communities

def portal_page(args):
  """
  This retrieves a page from the database for the community portal
  """
  page = None
  if "id" in args:
    page = fetch_one_from_db(Page, {"id": args["id"]})
  elif "name" in args:
    page = fetch_one_from_db(Page, {"name": args["name"]})
  return page

def portal_page2(args):
  """
  This also retrieves a page by name or id
  """
  if "id" in args:
    return Page.objects.filter(id=args["id"]).first()
  elif "name" in args:
    return Page.objects.filter(name=args["name"]).first()
  return page


def portal_page3(args):
  """
  This also retrieves a page by name or id.

  Warning.  only use this method if you know the page id or name exists
  """
  if "id" in args:
    try:
      return Page.objects.get(id=args["id"])
    except Exception as e:
      return None
  elif "name" in args:
    try:
      return Page.objects.get(name=args["name"])
    except Exception as e:
      return None
  return page
