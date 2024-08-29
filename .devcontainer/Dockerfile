FROM mcr.microsoft.com/devcontainers/miniconda:1-3

# Copy environment.yml (if found) to a temp location so we update the environment. Also
# copy "noop.txt" so the COPY instruction does not fail if no environment.yml exists.
COPY environment.yml* .devcontainer/noop.txt /tmp/conda-tmp/
RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/conda env update -n base -f /tmp/conda-tmp/environment.yml; fi \
    && rm -rf /tmp/conda-tmp

# [Optional] Uncomment to install a different version of Python than the default
# RUN conda install -y python=3.6 \
#     && pip install --no-cache-dir pipx \
#     && pipx reinstall-all

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# this might be necessary below

# Install any needed packages specified in requirements.txt
RUN curl -fsSL https://ollama.com/install.sh | sh
# RUN bash setup_dependencies.sh
# install chromadb
RUN pip install --q chromadb

#install langchain tools
RUN pip install --q unstructured langchain langchain-text-splitters
RUN pip install --q "unstructured[all-docs]"
RUN pip install --q langchain_community

#install flask
RUN pip install --q flask

#execute permissions
#COPY setup-ollama.sh /tmp/setup-ollama.sh
#RUN chmod +x /tmp/setup-ollama.sh
# RUN ollama pull mistral
#RUN /tmp/setup-ollama.sh

# Make port 80 available to the world outside this container
#EXPOSE 80

#run ollama when the container starts
#CMD ["ollama", "serve"]
# Run app.py when the container launches
#CMD ["python", "app.py"]
