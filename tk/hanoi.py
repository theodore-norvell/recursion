import random

class Hanoi :
    def __init__( self, count) :
        self._count = count
        self._spindles = [ [], [], [] ] 
        self._locations = []
        for i in range(0, count) :
            self._locations.append( 0 ) 
            self._spindles[0] = [ i ] + self._spindles[0]
        self.checkInvariant()

    def move( self, a, b ) :
        self.checkInvariant()
        assert 0 <= a and a < 3, "precondition: first argument should be 0, 1, or 2"
        assert 0 <= b and b < 3, "precondition: second argument should be 0, 1, or 2"
        if a==b : return 
        aCount = len( self._spindles[a] )
        assert aCount > 0, "precondition: source spindle is empty"
        d = self._spindles[a][ aCount-1 ]
        assert ( len( self._spindles[b] ) == 0
               or self._spindles[b][ len( self._spindles[b] )-1 ] > d
               ), "precondition error: larger disk on destination spindle"
        self._spindles[a] = self._spindles[a][0:aCount-1]
        self._spindles[b] = self._spindles[b] + [ d ]
        self._locations[ d ] = b
        self.checkInvariant()

    def checkInvariant( self ) :
        assert len( self._spindles ) == 3 , "invariant"
        for i in range( 0, 3 ) :
            s = self._spindles[i]
            for k in range( 0, len( s ) ) :
                d = s[k]
                assert 0 <= d and d < self._count, "invariant"
                assert self._locations[d] == i, "invariant"
                assert k==0 or d < s[k-1], "invariant"
        assert len( self._locations ) == self._count, "invariant"
        for i in range( 0, self._count ) :
            s = self._locations[i]
            assert i in self._spindles[s], "invariant"

    def draw( self ) :
        for i in range(0,3) :
            print( "" + str(i) + ": ", end="" )
            for d in self._spindles[ i ] :
                print( d, " ", end="" )
            print()
        print(self._locations)

    def whereIs( self, d ) :
        return self._locations[d]

    def scramble( self ) :
        self._locations = [ random.randrange(0, 3) for d in range( 0, self._count )  ]
        self._spindles = [[], [], []]
        for d in range( 0, self._count ) :
            l = self._locations[d]
            self._spindles[l].insert(0, d)
        self.draw()
        self.checkInvariant()
