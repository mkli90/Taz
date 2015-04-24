# -*- encoding: UTF-8 -*-
__author__ = 'Max'

from os import sys


class Game(object):
    class GameExitException(Exception):
        def __init__(self):
            pass

    class StackEmptyError(Exception):
        def __init__(self):
            pass

    class TriedToRegisterNotASceneError(Exception):
        def __init__(self):
            pass

    class SceneAlreadyRegisteredError(Exception):
        def __init__(self):
            pass

    class NoRegisteredSceneWithThisIDError(Exception):
        def __init__(self):
            pass

    class ParameterNotDictionaryError(Exception):
        def __init__(self):
            pass

    class IDisNotAStringError(Exception):
        def __init__(self):
            pass

    def __init__(self, uc, rc):
        self.scene_stack = []
        self.registered_scenes = {}

        if not self.param_is_dictionary(uc) or not self.param_is_dictionary(rc):
            raise Game.ParameterNotDictionaryError

        self.update_context = uc
        self.render_context = rc

    def param_is_dictionary(self, param):
        return type(param) == dict

    def register_new_scene(self, scene):
        if not self.is_an_instance_of(scene):
            raise Game.TriedToRegisterNotASceneError
        if self.is_scene_already_registered(scene):
            raise Game.SceneAlreadyRegisteredError

        scene.game = self
        self.registered_scenes[scene.get_identifier()] = scene
        self.update_all_scenes_registered_scenes()

        return True

    @staticmethod
    def is_an_instance_of(scn):
        return isinstance(scn, Scene) or scn == Scene

    def is_scene_already_registered(self, scene):
        for scene_name in self.registered_scenes:
            if scene_name == scene.get_identifier():
                return True
        return False

    def update_all_scenes_registered_scenes(self):
        for scene in self.registered_scenes.iteritems():
            scene[1].registered_scenes = self.registered_scenes

    def size_of_stack(self):
        return len(self.scene_stack)

    def push_scene_on_stack(self, ident):
        try:
            if not self.is_a_string(ident):
                raise Game.IDisNotAStringError

            self.pause_current_scene()
            scene_to_push = self.registered_scenes[ident]
            scene_to_push.init_scene()
            self.scene_stack.insert(0, scene_to_push)
        except KeyError:
            raise Game.NoRegisteredSceneWithThisIDError

    @staticmethod
    def is_a_string(ident):
        return type(ident) == str

    def pause_current_scene(self):
        if not self.is_stack_empty():
            self.scene_stack[0].tear_down()

    def is_stack_empty(self):
        return self.size_of_stack() == 0

    def pop_last_scene(self):
        return self.size_of_stack() == 1

    def pop_scene_from_stack(self):
        if self.is_stack_empty():
            raise Game.StackEmptyError
        if self.pop_last_scene():
            raise Game.GameExitException

        self.pause_old_scene(self.scene_stack[0])
        self.scene_stack.pop(0)
        self.resume_new_scene(self.scene_stack[0])

    @staticmethod
    def pause_old_scene(oldscene):
        oldscene.tear_down()

    @staticmethod
    def resume_new_scene(newscene):
        newscene.resume()

    def get_name_of_top_scene(self):
        topscene = self.get_top_scene()
        return topscene.get_identifier()

    def get_top_scene(self):
        if self.is_stack_empty():
            raise Game.StackEmptyError

        return self.scene_stack[0]

    def enter_mainloop(self):
        while True:
            self.get_top_scene().update(self.update_context)
            self.get_top_scene().render(self.render_context)


class Scene(object):
    def __init__(self, ident):
        self.game = None

        self.identifier = ident
        self.paused = False
        self.registered_scenes = {}

    def get_identifier(self):
        return self.identifier

    def is_paused(self):
        return self.paused

    def knows_registered_scenes(self):
        return len(self.registered_scenes) > 0

    def init_scene(self):
        self.paused = False

    def update(self, update_context):
        pass

    def render(self, render_context):
        pass

    def tear_down(self):
        self.paused = True

    def resume(self):
        self.paused = False



