import unittest
import pygame
import player



def create_key_mock(pressed_key):
    def helper():
        tmp = [0] * 300
        tmp[pressed_key] = 1
        return tmp
    return helper



class TestPlayer(unittest.TestCase):
    

    def test_get_status(self):
    
       

       self.assertEqual(player.get_input(pygame.K_RIGHT), create_key_mock(pygame.K_RIGHT))






if __name__ == '__main__':
    unittest.main()