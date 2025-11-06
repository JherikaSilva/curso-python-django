from lista import rotacionar_lista

def test_rotacionar_lista():
   
   assert rotacionar_lista([1,2,3,4,5], 2) == [4,5,1,2,3]