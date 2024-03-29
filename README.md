<!---
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. See accompanying LICENSE file.
-->

# What is Hadoop Submarine?  [![Build Status](https://travis-ci.org/pingsutw/Submarine-SDK.svg?branch=master)](https://travis-ci.org/pingsutw/Submarine-SDK)

Submarine is a new subproject of Apache Hadoop.

Submarine is a project which allows infra engineer / data scientist to run
*unmodified* Tensorflow or PyTorch programs on YARN or Kubernetes.

Goals of Submarine:
- It allows jobs easy access data/models in HDFS and other storages.
- Can launch services to serve Tensorflow/PyTorch models.
- Support run distributed Tensorflow jobs with simple configs.
- Support run user-specified Docker images.
- Support specify GPU and other resources.
- Support launch tensorboard for training jobs if user specified.
- Support customized DNS name for roles (like tensorboard.$user.$domain:6006)

# Submarine-SDK

- Allow data scients to track distributed ML job 
- Support store ML parameters and metrics in Submarine-server
- Support store ML job output (e.g. csv,images)
- Support hdfs,S3 and mysql 
- (Submarine-DB) metric and param instance in submarine-server database 
- (Submarine-DB) Support REST Api for submarine server 
- (WEB) Metric tracking ui in submarine-web
- (WEB) Metric graphical display in submarine-web
