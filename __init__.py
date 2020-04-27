# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import os


# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

# TODO: Change "Template" to a unique name for your skill
class PiSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(PiSkill, self).__init__(name="Pi")

    @intent_handler(IntentBuilder("").require("Status").require("Hardware"))
    def disable_enable_monitor_intent(self, message):
        if message.data["Hardware"] == "monitor":
            if message.data["Status"] == "enable":
                os.system('vcgencmd display_power 1')           
            else:
                os.system('vcgencmd display_power 0')
        elif message.data["Hardware"] == "pi":
            if message.data["Status"] == "restart" or message.data["Status"] == "reboot":
                os.system('sudo reboot')
            
    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return PiSkill()
