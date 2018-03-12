iUTAHData
=========

This project contains the code for the iUTAH Modeling and Data Federation website - data.iutahepscor.org.

<p align="center"><img src="https://github.com/UCHIC/iUTAHData/raw/master/doc/images/data.jpg"></p>

Installation
============
iUTAHData uses Django and Python 2.7.

Once you have cloned or downloaded the repository, install python dependencies with `pip install -r requirements.txt`

When installing packages in `requirements.txt` you may get an error dealing with `pyodbc`.
Installing [iODBC](http://www.iodbc.org/) on your system should fix this error.

**Linux/Debian**

```
sudo apt-get install libiodbc2 iodbc msodbcsql
```

**macOS** (using [HomeBrew](https://brew.sh/))

```
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
brew update
brew install --no-sandbox msodbcsql@13.1.9.2 mssql-tools@14.0.6.0 unixodbc
```

It might be necessary to connect to the production database during
development, testing, or deployment. The production database runs on a
Microsoft SQL Server (MSSQL).
For developers working on a unix system, you will need to configure
[FreeTDS](http://www.freetds.org/faq.html#What.is.FreeTDS) on your system
to connect to an MSSQL server.

> FreeTDS is a set of libraries for Unix and Linux that allows your programs to natively talk to Microsoft SQL Server and Sybase databases.

For the purposes of iUTAHData, FreeTDS uses the drivers provided by
iODBC to communicate with the MSSQL production database from a unix system.

For Linux/Debian users:

1. Install FreeTDS: `sudo apt-get install freetds-bin tdsodbc`
2. Create a Database Server Name (DSN) configuration file

For Mac users:

1. Install FreeTDS: `brew install freetds`
2. Create a Database Server Name (DSN) configuration file

Sponsors
---------

![iUTAH](/doc/images/iutah_eu_horz_sm.png)    ![NSF](/doc/images/nsf.gif)

This material is based on work supported by National Science Foundation Grant EPS 1208732 awarded to Utah State University.  Any opinions, findings, and conclusions or recommendations expressed are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.

Copying and License
----------------------------

This material is copyright (c) 2013 Utah State University.

It is open and licensed under the New Berkeley Software Distribution (BSD) License.  Full text of the license follows.

Copyright (c) 2013, Utah State University. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

*  Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
*  Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
*  Neither the name of Utah State University nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. 



