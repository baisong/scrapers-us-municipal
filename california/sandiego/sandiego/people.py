from pupa.scrape import Scraper, Person
import lxml.html

class SandiegoPersonScraper(Scraper):

    def scrape(self):
        url = "https://www.sandiego.gov/citycouncil"
        entry = self.get(url).text
        page = lxml.html.fromstring(entry)
        page.make_links_absolute(url)

        for position in page.xpath("//*[@id='block-system-main']/div/div[2]/div/main/div/div/divdiv[contains(@class, 'card__wrap')]"):
            position_name = "Councilmember"
            name = position.xpath('../div/h2')[0].text
            name = name.replace("Councilmember","").strip()
            homepage = position.xpath("../div/p[1]/a")[0].href
            member = Person(name=name,
                role=position_name,
                primary_org="committee")
            member.add_link(homepage)
            member.add_source(url)
            yield member