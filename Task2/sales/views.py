from django.shortcuts import render
from rest_framework import generics
from .models import SalesModel
from .serializers import MyModelSerializer
from django.shortcuts import render
import matplotlib.pyplot as plt
import matplotlib
# import pandas as pd
from django.db import connection
from django.http import HttpResponse
# Set the backend to use for matplotlib
matplotlib.use('TkAgg')  # Use the appropriate backend for your system (e.g., 'TkAgg', 'Qt5Agg', etc.)




class MyModelListCreateView(generics.ListCreateAPIView):
    queryset = SalesModel.objects.all()
    serializer_class = MyModelSerializer

class MyModelRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesModel.objects.all()
    serializer_class = MyModelSerializer

from asgiref.sync import sync_to_async
# Configure matplotlib to work in the main thread
import threading
matplotlib.interactive(False)
matplotlib.pyplot.switch_backend('agg')
threading.Thread(target=matplotlib.pyplot.ion()).start()

@sync_to_async

def generate_chart(request):
    labels = ['Label 1', 'Label 2', 'Label 3']
    sizes = [30, 50, 20]
    colors = ['red', 'green', 'blue']

    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart appears as a circle

    # Save the chart to a temporary file
    # chart_path = './images/chart.png'
    chart_path = '/Users/cio/UpdateTech/Task2/sales/templates/pie.png'
    plt.savefig(chart_path)



    # Data for the line chart
    x = [1, 2, 3, 4, 5]
    y = [10, 25, 15, 30, 20]

    # Generate the line chart
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Chart')

    # Save the chart to a temporary file
    chart_image_path = '/Users/cio/UpdateTech/Task2/sales/templates/line.png'
    plt.savefig(chart_image_path)


    chart_image_path = '/Users/cio/UpdateTech/Task2/sales/templates/'
    # Return the path to the chart image
    return render(request, 'report.html', {'chart_image_path': chart_image_path})




def show_query_result(request):
    # Write your SQL query
    query1 = "SELECT EXTRACT(year FROM order_date) AS year, COUNT(*) AS total_orders FROM sales_salesmodel GROUP BY YEAR(order_date) ORDER BY year;"
    query2 = "SELECT COUNT(DISTINCT customer_id) AS total_customers FROM sales_salesmodel;"
    query3 = "SELECT customer_id, COUNT(*) AS order_count FROM orders GROUP BY customer_id sales_salesmodel BY order_count DESC LIMIT 3;"
    query4 = "SELECT customer_id, COUNT(*) AS order_count FROM sales_salesmodel GROUP BY EXTRACT(year FROM order_date) AS year;"
    query5 = "SELECT sub_category FROM sales_salesmodel ORDER BY sub_category DESC;"
    
    # Execute the SQL query
    queries = [query1, query2, query3, query4, query5]
    result_str = ''

    with connection.cursor() as cursor:
        for i in range(5):
            cursor.execute(queries[i])
            result = cursor.fetchall()

            # Convert the result to a string for display
            result_str = "\n".join(str(row) for row in result)

    # Render the result in a template or return as an HTTP response
    # Example using HttpResponse:
    return HttpResponse(result_str)
