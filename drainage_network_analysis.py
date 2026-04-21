import csv
import os
from qgis.core import QgsProject, QgsMapLayerType, QgsWkbTypes

layer = iface.activeLayer()

if not layer:
    print("Error: No active layer selected. Please click on your drainage lines layer.")
elif layer.type() != QgsMapLayerType.VectorLayer:
    print(f"Error: You selected '{layer.name()}', which is a Raster. Please select a Vector layer.")
else:
    if layer.geometryType() != QgsWkbTypes.LineGeometry:
        print(f"Warning: Selected layer '{layer.name()}' is not a Line layer.")

    project_path = QgsProject.instance().homePath()
    output_file = os.path.join(project_path, 'Drainage_Network_Report.csv')

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Channel_ID', 'Feature_Type', 'Length_meters', 'Risk_Category'])

        for feature in layer.getFeatures():
            feat_id = feature.id()
            geom = feature.geometry()
            
            if geom and not geom.isNull():
                length = geom.length()
                length_rounded = round(length, 2)
                
                risk = "High Runoff" if length > 100 else "Standard Drainage"
                writer.writerow([f"CHNL-{feat_id}", "Drainage Line", length_rounded, risk])

    print("-" * 50)
    print("SUCCESS: Hydrology report automatically exported to:")
    print(output_file)
    print("Ready for Stormwater Management Engineers.")
    print("-" * 50)
