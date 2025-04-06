FROM openjdk:11

ENV SPARK_VERSION=3.5.0
ENV HADOOP_VERSION=3
ENV SCALA_VERSION=2.12

# Install Python, pip, curl
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Spark
RUN curl -O https://archive.apache.org/dist/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz && \
    tar -xzf spark-3.5.0-bin-hadoop3.tgz && \
    mv spark-3.5.0-bin-hadoop3 /opt/spark && \
    ln -s /opt/spark/bin/spark-submit /usr/bin/spark-submit

ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

# Set workdir
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip3 install -r requirements.txt

# Run app
CMD ["spark-submit", "app.py"]
