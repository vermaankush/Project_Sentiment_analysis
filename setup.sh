#setup.sh is the script program for bash and it helps us to execute the code with respect to the installation of requirements.txt andit also helps you to setup
#the environement for the streamlit library.
mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
