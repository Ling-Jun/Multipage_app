import dash

app = dash.Dash(__name__, suppress_callback_exceptions=True,
# When we're adding callbacks to elements that don't exist in the app.layout, 
# Dash will raise an exception to warn us that we might be doing something wrong. 
# In this case, we're adding the elements through a callback, so we can ignore the exception by 
# setting suppress_callback_exceptions=True. It is also possible to do this without suppressing callback exceptions. 
# See the example below for details. 
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
# There is a method to let web designers take control over the viewport (the user's visible area of a web page), 
# through the <meta> tag. meta_tags are required for the app layout to be mobile responsive
server = app.server
