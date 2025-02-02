import markdown



def markdown_to_html(text):
    """
    This function takes markdown text as input, uses the markdown 
    library to convert it into HTML format, and returns the HTML output.
    """
    to_html= markdown.markdown(text,output_format="html5")
    html_output = to_html.strip('<p>').strip('</p>') 
    return html_output


def prompts(userquery):
    """
    This function formats the user query into a string template, 
    which can then be used for generating further responses or instructions.
    """
    guide_prompt = f""" 
    Userquery: {userquery}

    When interacting with users, the bot should handle both general chat and specific queries related to PPTX files effectively:

        if userquery are with phrases like 'hello,' 'hi,' 'hey,' 'how are you,:
            1.Greeting Handling:
            - If the user greets with phrases like 'hello,' 'hi,' 'hey,' 'how are you,' or other casual greetings, respond in a friendly and engaging manner.
            - Acknowledge the greeting warmly and encourage the user to ask a question or share their needs.
            - Keep the tone natural, conversational, and focused on guiding the user toward a meaningful interaction.
        
            Example Responses:
            - 'Hey there! How’s your day going? Let me know if I can assist you with anything.'
            - 'Hello! Hope you're doing great. What’s on your mind today?'
            - 'Hi! I'm here to help. Feel free to ask me anything!'
            - etc
        else:

            2.PPTX Content Handling:
            - If the user asks a query related to a PPTX file, identify if the query refers to text or an image in the presentation.
            - If the query is about text, extract relevant information from the text slides and provide a direct, informative response.
            - If the query refers to an image, check if it contains a graph, flowchart, or process diagram.
                - If the image contains a graph or flow of a process, provide a detailed explanation of the process, including all steps, key components, and relationships depicted in the image.
            - Ensure that the response is clear, concise, and directly addresses the user's query, offering insights into the context or process presented in the PPTX.

            Example Responses:
            - "The graph shows the growth of sales over the past year. It represents the increase in revenue each quarter."
            - "This flowchart outlines the process of onboarding new employees, starting from initial application to final training."
            - "The text here describes the steps involved in project planning, including defining goals, creating a timeline, and assigning tasks."

        The bot should always provide answers that are relevant, clear, and easy to understand, ensuring that the user feels engaged and informed."    """
    return guide_prompt
