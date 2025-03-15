import scrapy
from jobs.models import Job

class JobSpider(scrapy.Spider):
    name = "jobs"
    start_urls = ["https://www.naukri.com/product-manager-jobs"]

    def parse(self, response):
        for job in response.css(".jobTuple"):
            job_data = {
                "title": job.css(".title::text").get(),
                "company": job.css(".company::text").get(),
                "location": job.css(".location::text").get(),
                "experience": job.css(".experience::text").get(),
                "apply_link": job.css("a::attr(href)").get()
            }
            Job.objects.create(**job_data)
