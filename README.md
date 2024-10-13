# Nginx-Log-Analyzer
A DevOps Project Idea

Been looking into more 'code and project' based stuff while out of work at the moment and caring for family, so I need something I can pickup and drop in an instant should the need arise.

Checking on the DevOps Project Ideas Roadmap - [Link](https://roadmap.sh/devops/projects) I saw this was a quick one I might be able to bash my brain against.

Ended up with a Python and Bash version of the script, the latter using things like awk, sort, and uniq.

# Instructions

To run either of these scripts you have to make it executable by running:

```
# Python:
chmod +x python_log_analyzer.py 

# Bash:
chmod +x bash_log_analyzer.sh
```

Now you can run the script from the command line and pass it the path to the log file:

```
python3 .\python_log_analyzer.py \<PATH THE LOGFILE>
```

An example of this running in Python:

![Screenshot](https://github.com/ha3ks/Nginx-Log-Analyzer/blob/main/screenshot.png)

