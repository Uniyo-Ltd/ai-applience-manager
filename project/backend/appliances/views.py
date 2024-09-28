from django.shortcuts import render
from .models import Appliance, Order
from django.http import HttpResponse
from django.template.loader import render_to_string

def appliance_list(request):
    appliances = list(Appliance.objects.values())
    return JsonResponse(appliances, safe=False)

def replacement_options(request):
    appliances = Appliance.objects.all()
    html_content = "<h1>Recommended Appliance Replacement Options</h1>\n"
    html_content += "<table>\n"
    for appliance in appliances:
        html_content += f"""
        <tr>
            <td>{appliance.model}</td>
            <td>{appliance.price}</td>
            <td>{appliance.specification}</td>
            <td><button onclick="showModal({appliance.id})">Order</button></td>
        </tr>
        """
    html_content += "</table>\n"

    html_content += """
    <script>
    function showModal(applianceId) {{
        var modal = document.getElementById('modal');
        modal.style.display = 'block';
        var appliance = fetch('/order/?appliance_id=' + applianceId)
            .then(response => response.json())
            .then(data => {{
                document.getElementById('model').textContent = data.model;
                document.getElementById('price').textContent = data.price;
                document.getElementById('specification').textContent = data.specification;
            }})
            .catch(error => console.error('Error:', error));
    }}

    function closeModal() {{
        var modal = document.getElementById('modal');
        modal.style.display = 'none';
    }}
    </script>

    <div id="modal" style="display:none;">
        <h2>Schedule Delivery of Selected Appliance</h2>
        <p>Model: <span id="model"></span></p>
        <p>Price: <span id="price"></span></p>
        <p>Specification: <span id="specification"></span></p>
        <button onclick="closeModal()">Close</button>
    </div>
    """
    
    return HttpResponse(html_content)




def order_appliance(request, appliance_id):
    appliances = Appliance.objects.all()
    html_content = ""
    for appliance in appliances:
        html_content += f"<tr><td>{appliance.model}</td><td>{appliance.price}</td><td>{appliance.specification}</td><td><button onclick=\"showModal({appliance.id})\">Order</button></td></tr>"
    
    html_content += """
    <table>
        {html_content}
    </table>

    <script>
    function showModal(applianceId) {{
        var modal = document.getElementById('modal');
        modal.style.display = 'block';
    }}

    function closeModal() {{
        var modal = document.getElementById('modal');
        modal.style.display = 'none';
    }}
    </script>

    <div id="modal" style="display:none;">
        <h2>Schedule Delivery of Selected Appliance</h2>
        <p>Model: <span id="model"></span></p>
        <p>Price: <span id="price"></span></p>
        <p>Specification: <span id="specification"></span></p>
        <button onclick=\"closeModal()\">Close</button>
    </div>

    <script>
    function populateModal(applianceId) {{
        fetch('/order/?appliance_id=' + applianceId)
            .then(response => response.json())
            .then(data => {{
                document.getElementById('model').textContent = data.model;
                document.getElementById('price').textContent = data.price;
                document.getElementById('specification').textContent = data.specification;
            }})
            .catch(error => console.error('Error:', error));
    }}
    </script>
    """
    
    return HttpResponse(html_content.format(html_content=html_content))