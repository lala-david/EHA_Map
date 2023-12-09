from flask import Flask, request, send_file
import folium
import random
import uuid

app = Flask(__name__)

@app.route('/mapIntegratedOutcomeReport', methods=['POST'])
def map_report():
    marker_data = request.get_json()

    m = folium.Map(location=[marker_data[0]["위도"], marker_data[0]["경도"]], zoom_start=21)

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
        """ % (data['화학 위해도'], data['생태독성 위해도'], data['생태 위해도'], bg_color, border_color)

        iframe = folium.IFrame(html=chart_html, width=280, height=280)
        popup = folium.Popup(iframe, max_width=2650)
        marker = folium.Marker(location=[data['위도'], data['경도']], popup=popup)
        marker.add_to(m)

    for data in marker_data:
        create_marker(data)

    filename = 'map_' + str(uuid.uuid4()) + '.html'
    m.save(filename)
    
    return send_file(filename, mimetype='text/html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8200)