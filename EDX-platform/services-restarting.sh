#!/bin/sh

# restart edx instances
sudo /edx/bin/supervisorctl restart lms
sudo /edx/bin/supervisorctl restart cms
sudo /edx/bin/supervisorctl restart edxapp_worker:
