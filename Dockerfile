FROM python3

LABEL maintainer="kaiocunha" 
LABEL version="1.0" 
LABEL description="docker image for data science development env"  

RUN pip3 install numpy pandas matplotlib plotly dash

# EXPOSE 8888

# CMD [ "jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root" ]