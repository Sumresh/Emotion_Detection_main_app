import cohere
co = cohere.Client('QxGBcMk2UbsaXJ9ryPc33GRoyxrUBLoPC9tcqMqf')
def from_cohere(text, emotion):
    custom_query = f"for this text : '{text}'. I got '{emotion} list with their respective probabilities' as result. so I need you to summerize the '{text}' how this text is '{emotion}'. please make the response be 2 lines short and precise."
    response = co.generate(
    prompt=custom_query,
    )
    print(response)
    return response[0].text