import gradio as gr
from gradio.components.number import Number


# def greet(name, intensity):
#     return "Hello, " + name + "!" * int(intensity)
#
#
# demo = gr.Interface(
#     fn=greet,
#     inputs=["text", "slider"],
#     outputs=["text"],
#     flagging_mode="never"
# )


def calc_area(width, height):
    return f"The area is {width*height}"


demo = gr.Interface(
    fn=calc_area,
    inputs=["slider", "slider"],
    # inputs=["number", "number"],
    # inputs=[Number(label="Insert width:"), Number(label="Insert height")],
    outputs=["text"],
    flagging_mode="never",
    submit_btn="Calculate"
)


demo.launch(share=False)
