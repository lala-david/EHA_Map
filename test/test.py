import folium
import json
import random
import os 

m = folium.Map(location=[35.964362, 126.736021], zoom_start=21)

with open('marker_data.json', 'r') as file:
    marker_data = json.load(file)

def create_marker(data):
    bg_color = 'rgba({}, {}, {}, 0.2)'.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    border_color = 'rgba({}, {}, {}, 1)'.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    chart_html = """
    <canvas id="chart" width="200" height="200"></canvas>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        var ctx = document.getElementById('chart').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'radar',
            data: {
                labels: ['Chem-LoE', 'Ecop_LoE', 'Ecootox-LoE'],
                datasets: [{
                    label: 'Marker Data',
                    data: [%s, %s, %s],
                    backgroundColor: '%s',
                    borderColor: '%s',
                    borderWidth: 1
                }]
            },
            options: {
                scale: {
                    ticks: {
                        beginAtZero: true,
                        max: 1
                    }
                }
            }
        });
    </script>
    """ % (data['Chem-LoE'], data['Ecop_LoE'], data['Ecootox-LoE'], bg_color, border_color)

    iframe = folium.IFrame(html=chart_html, width=250, height=250)
    popup = folium.Popup(iframe, max_width=2650)
    marker = folium.Marker(location=data['coordinates'], popup=popup)
    marker.add_to(m)

for data in marker_data:
    create_marker(data)

m.save('map.html')
os.system('map.html')