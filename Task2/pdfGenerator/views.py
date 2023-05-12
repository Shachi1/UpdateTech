from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from sales import SalesModel

class PDFReportView(View):
    def get(self, request):
        # Fetch the dataset for the report (replace with your own dataset retrieval logic)
        dataset = SalesModel.objects.all()  # Assuming you have a model named `YourModel`

        # Render the report template with the dataset
        report_html = render_to_string('report.html', {'dataset': dataset})

        # Create a PDF object from the HTML content
        pdf = HTML(string=report_html).write_pdf()

        # Create the HttpResponse object with PDF headers
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'

        # Write the PDF content to the response
        response.write(pdf)

        return response
