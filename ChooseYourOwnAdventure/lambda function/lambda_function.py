# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome to Choose Your Own Adventure. What kind of story would you like to hear?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class SelectAGenreIntentHandler(AbstractRequestHandler):
    """Handler for Select A Genre Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SelectAGenre")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        genre = handler_input.request_envelope.request.intent.slots["SelectedGenre"].resolutions.resolutions_per_authority[0].values[0].value.name
        logger.debug(genre)
        if genre == "Science Fiction":
            speak_output = """"Watch your speed coming in youngun'," cries the captain. You doze at your console as the first mate's daughter maneuvers the great ship into Bay 17. The greatest spaceport in the galaxy, Landon Station, engulfs your battlecruiser. Startling awake to Jophur's strong punch in the arm, you gaze in wonder at the creatures and mechs guiding the ship in. What do you do? Go below decks with Jophur to find the no-good cook that owes you money, or scamper off the ship at the first chance you get?"""
            ask_output = "What do you do? Go below decks with Jophur to find the no-good cook that owes you money, or scamper off the ship at the first chance you get?"
        else:
            speak_output = """"Avast ye scurvy dogs," cries the captain. You doze in the crow's nest as the crew maneuvers the great ship into the busy port. Landon City, the great city of adventure, sprawls out before you. Startling awake to Jophur's strong punch in the arm, you gaze in wonder at the mayhem below as the crew lowers the gang plank and prepares to disembark. What do you do? Go below decks with Jophur to find the no-good cook that owes you money, or scamper off the ship at the first chance you get?"""
            ask_output = "What do you do? Go below decks with Jophur to find the no-good cook that owes you money, or scamper off the ship at the first chance you get?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(ask_output)
                .response
        )


class GetMoneyIntentHandler(AbstractRequestHandler):
    """Handler for Get Money Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("GetMoney")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        speak_output = """You follow Jophur below decks. Turning a corner you see a flash and hear a shot ring out. Suddenly the world starts to spin. Oh no! The last thing you see is the good-for-nothing cook handing a purse to Jophur. You realize too late that you've been betrayed. The End."""

        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_should_end_session(True)
                .response
        )

class GetOffTheShipIntentHandler(AbstractRequestHandler):
    """Handler for Get Off The Ship Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("GetOffTheShip")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        speak_output = """You decide to forsake your loot and bid Jophur a fond goodbye as you head off into the port on your own. There are people and creatures everywhere, bustling to and fro. While the cacophony nearly deafens you, it is the smell that draws you in. The intoxicating aroma wafting from a nearby shipment of spice overwhelms your senses. But what wonders there are to behold. To your left, a person with blue skin catches your eye as they dart through the crowd. To your right, a large creature is reluctantly goaded toward the ship. Suddenly, it shucks its bonds and charges off, smashing through the spice shipment, throwing boxes everywhere, and spilling the precious spice. Do you chase after the blue-skinned stranger, do you grab one of the cases of spice and run away, or do you help to gather and preserve the spice, helping the poor soul crying over the mess?"""
        ask_output = "Do you chase after the blue-skinned stranger, do you grab one of the cases of spice and run away, or do you help to gather and preserve the spice, helping the poor soul crying over the mess?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(ask_output)
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Thanks for asking for help. Try saying Tell me a Fantasy Fiction story, or tell me a sci fi story."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. Try saying Tell me a Fantasy Fiction story, or tell me a sci fi story. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(SelectAGenreIntentHandler())
sb.add_request_handler(GetMoneyIntentHandler())
sb.add_request_handler(GetOffTheShipIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()