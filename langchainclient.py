from langserve import RemoteRunnable

# Create an instance of RemoteRunnable that points to a remote chain URL
remote_chain = RemoteRunnable("http://localhost:8000/chain/")

# Invoke the remote chain with a dictionary containing the language and text as input
# The input dictionary has two keys: 'language' set to 'italian' and 'text' set to 'hi'
# The result from the remote server will be printed
print(remote_chain.invoke({"language": "italian", "text": "hi"}))

# running command "python langchainclient.py"