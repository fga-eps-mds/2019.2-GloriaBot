# from typing import Dict, Text, Any, List, Union, Optional

# from rasa_sdk import Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormAction


# class RestaurantForm(FormAction):
#     """Example of a custom form action"""

#     def name(self) -> Text:
#         """Unique identifier of the form"""

#         return "restaurant_form"

#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""

#         return ["feedback"]

#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
#         """A dictionary to map required slots to
#             - an extracted entity
#             - intent: value pairs
#             - a whole message
#             or a list of them, where a first match will be picked"""

#         return {
#             "feedback": [self.from_entity(entity="feedback"), self.from_text()],
#         }


#     def submit(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict]:
#         """Define what the form has to do
#             after all required slots are filled"""

#         # utter submit template
#         dispatcher.utter_template("utter_submit", tracker)
#         return []

