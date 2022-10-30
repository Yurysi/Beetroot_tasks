"""
TV controller

Create a simple prototype of a TV controller in Python. It’ll use the
following commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel
numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the
last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is
the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and
returns "Yes", if the channel N or 'name' exists in the list, or "No" - in
the other case.


The default channel turned on before all commands is №1.

Your task is to create the TVController class and methods described above.
"""

channels = ["BBC", "Discovery", "TV1000"]


class TvController:
    def __init__(self, channels_list: list):
        self.channels = channels_list
        self.choosen_channel = self.channels[0]

    def first_channel(self):
        self.choosen_channel = self.channels[0]
        return self.choosen_channel

    def last_channel(self):
        self.choosen_channel = self.channels[-1]
        return self.choosen_channel

    def turn_channel(self, u_value):
        self.u_value = u_value
        try:
            self.choosen_channel = self.channels[int(self.u_value) - 1]
            return self.choosen_channel
        except IndexError:
            return f'I have only {len(self.channels)} channels'
        except ValueError:
            return 'Please enter numbers.'

    def next_channel(self):
        num = self.channels.index(self.choosen_channel) + 1
        if num < len(self.channels):
            self.choosen_channel = self.channels[num]
            return self.choosen_channel
        else:
            self.choosen_channel = self.channels[0]
            return self.choosen_channel

    def previous_channel(self):
        num = self.channels.index(self.choosen_channel) - 1
        if num < len(self.channels):
            self.choosen_channel = self.channels[num]
            return self.choosen_channel
        else:
            self.choosen_channel = self.channels[0]
            return self.choosen_channel

    def current_channel(self):
        return self.choosen_channel

    def is_exist(self, any_value):
        try:
            any_value = int(any_value)
            try:
                if self.channels[any_value - 1]:
                    return 'Yes'
            except:
                return "No"

        except:
            if any_value in self.channels:
                return 'Yes'
            elif any_value.upper() in self.channels:
                return 'Yes'
            elif any_value.title() in self.channels:
                return 'Yes'
            else:
                return 'No'


controller = TvController(channels)
print(controller.first_channel())

print(controller.last_channel())

print(controller.turn_channel(1))
print(controller.next_channel())

print(controller.previous_channel())

print(controller.current_channel())

print(controller.is_exist(4))

print(controller.is_exist("discovery"))
