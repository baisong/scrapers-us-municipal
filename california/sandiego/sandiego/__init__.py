# encoding=utf-8
from pupa.scrape import Jurisdiction, Organization
from .events import SandiegoEventScraper
from .people import SandiegoPersonScraper

class Sandiego(Jurisdiction):
    division_id = "ocd-division/country:us/state:ca/place:san_diego/council_district:1"
    classification = "government"
    name = "City of San Diego"
    url = "http://www.sandiego.gov"
    scrapers = {
        #"events": SandiegoEventScraper,
        "people": SandiegoPersonScraper,
    }

    def get_organizations(self):
        #REQUIRED: define an organization using this format
        #where org_name is something like Seattle City Council
        #and classification is described here:
        org = Organization(name="San Diego City Council", classification="legislature")

        # OPTIONAL: add posts to your organizaion using this format,
        # where label is a human-readable description of the post (eg "Ward 8 councilmember")
        # and role is the position type (eg councilmember, alderman, mayor...)
        # skip entirely if you're not writing a people scraper.
        org.add_post(label="Mayor", role="mayor")
        org.add_post(label="Councilmember, District 1", role="councilmember")
        org.add_post(label="Councilmember, District 2", role="councilmember")
        org.add_post(label="Councilmember, District 3", role="councilmember")
        org.add_post(label="Councilmember, District 4", role="councilmember")
        org.add_post(label="Councilmember, District 5", role="councilmember")
        org.add_post(label="Councilmember, District 6", role="councilmember")
        org.add_post(label="Councilmember, District 7", role="councilmember")
        org.add_post(label="Councilmember, District 8", role="councilmember")
        org.add_post(label="Councilmember, District 9", role="councilmember")

        #REQUIRED: yield the organization
        yield org
