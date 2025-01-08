FROM python:3.11.11-bullseye

WORKDIR /root

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    cd /usr/local/bin && \
    ln -s ~/.local/share/pypoetry/venv/bin/poetry && \
    poetry config virtualenvs.create false

# Copy all your package in the root directory of your image.
COPY ./ /root/

# Install dependencies with Poetry
RUN poetry install

# Set the default command to keep the container running
CMD ["tail", "-f", "/dev/null"]

