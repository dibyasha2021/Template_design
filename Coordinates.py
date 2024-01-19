# Necessary imports

from PIL import Image
import numpy as np
import plotly.express as px
import dash
from dash.dependencies import State 
from dash import Dash, dcc, html, Input, Output, no_update, callback
import json



image_path = r"DEMO\generated\beach_bannerbg03_1X1_500.jpg"  # Replace with the actual file path
img = Image.open(image_path, "r")

fig = px.imshow(img)
fig.update_layout(dragmode="drawrect")

app = Dash(__name__)
app.layout = html.Div(
    [
        html.H3("Select a region to see its characteristics"),
        dcc.Graph(id="graph-picture", figure=fig),
        dcc.Markdown("Characteristics of shapes"),
        html.Pre(id="annotations-data"),
    ]
)
shape_characteristics = {}
@callback(
    Output("annotations-data", "children"),
    Input("graph-picture", "relayoutData"),
    prevent_initial_call=True,
)

def on_new_annotation(relayout_data):
  if "shapes" in relayout_data:
      
      relayoutdata = json.dumps(relayout_data["shapes"], indent=2)
      
      return relayoutdata
  else:
      return no_update

if __name__ == "__main__":
    app.run(debug=True)

