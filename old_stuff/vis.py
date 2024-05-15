import gradio as gr
import numpy as np
import plotly.express as px
import pandas as pd
import json

pmf_tsne = json.load(open("pmf_tsne.json", "r"))
bpmf_tsne = json.load(open("bpmf_tsne.json", "r"))

reliability = json.load(open("reliability.json", "r"))
country = json.load(open("country.json", "r"))
political = json.load(open("political_leaning.json", "r"))

color_metrics = ["reliability", "country", "political"]

def newssource_representation(mode="pmf", color_by=["reliability"]):
    if mode == "pmf":
        newssources = list(pmf_tsne.keys())
        x, y, z = [], [], []
        for ns in newssources:
            x.append(pmf_tsne[ns][0])
            y.append(pmf_tsne[ns][1])
            z.append(pmf_tsne[ns][2])
    else:
        newssources = list(bpmf_tsne.keys())
        x, y, z = [], [], []
        for ns in newssources:
            x.append(bpmf_tsne[ns][0])
            y.append(bpmf_tsne[ns][1])
            z.append(bpmf_tsne[ns][2])
    
    # reliability
    reliability_color = []
    for ns in newssources:
        if ns not in reliability:
            reliability_color.append("unknown")
        else:
            reliability_color.append(reliability[ns])
    
    # country 
    country_color = []
    for ns in newssources:
        if ns not in country:
            country_color.append("unknown")
        else:
            country_color.append(country[ns])
    
    # political leaning
    political_color = []
    for ns in newssources:
        if ns not in political:
            political_color.append("unknown")
        else:
            political_color.append(political[ns])
    
    df = pd.DataFrame({"x": x, "y": y, "z": z, 
                       "reliability_color": reliability_color, 
                       "country_color": country_color,
                       "political_color": political_color,
                       "newssources": newssources})
    
    which_color_metric = "reliability_color"
    if color_by[0] == "country":
        which_color_metric = "country_color"
    elif color_by[0] == "political":
        which_color_metric = "political_color"
    else:
        which_color_metric = "reliability_color"
    fig = px.scatter_3d(df, x="x", y="y", z="z", 
                        color=which_color_metric, 
                        hover_name="newssources")
    fig.update_layout(legend=dict(
                    orientation="v",
                    yanchor="auto",
                    y=1,
                    xanchor="right",  # changed
                    x=-0.3
    ))
    fig.update_traces(marker_size=2)
    # fig.update_layout(width=800, height=800) 
    return fig

with gr.Blocks() as demo:
    gr.Markdown(
    """
    # Representing news sources in 3D
    Using embedding obtained from probabilistic matrix factorization.
    """)
    i1 = gr.Dropdown(["PMF", "BPMF"], label="Which method")
    i2 = gr.CheckboxGroup(color_metrics, label="Color by")
    gr.Examples([["PMF", ["reliability"]], ["PMF", ["country"]], ["PMF", ["political"]], 
                 ["BPMF", ["country"]], ["BPMF", ["country"]], ["BPMF", ["political"]]], inputs=[i1, i2])
    btn = gr.Button("Visualize")
    o1 = gr.Plot()
    gr.Markdown(
    """
    By Junita Sirait for COS513. 
    """)

    btn.click(fn=newssource_representation, inputs=[i1, i2], outputs=o1)



if __name__ == "__main__":
    demo.launch(share=True)