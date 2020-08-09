# for Hawthorn version and later
 
# 1. switch to Ubuntu username 'edxapp', and then simultaneously launch a bash shell
sudo -H -u edxapp bash
 
# 2. load the virtual environment for user 'edxapp' that is shipped with your Open edX installation
source /edx/app/edxapp/edxapp_env
 
# 3. switch to the Open edX "main" working directory (this is where the Paver executable as well as other Open edX utility apps are located)
cd /edx/app/edxapp/edx-platform
 
# 4. execute paver to recompile static assets for the LMS (Learning Management System) Django project.
#    this takes between 10 and 20 minutes to run, and generates a LOT of screen output.
paver update_assets lms --settings=production
 
# 5. (optional step) execute paver to recompile static assets for the CMS (Course Management Studio) Django project
paver update_assets cms --settings=production
