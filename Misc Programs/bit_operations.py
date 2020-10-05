import re

class Number:
    def __init__( self, v ):
        # intialize the object
        self.v = v
    def toString( self ):
        # print the number in mulitple formats: decimal, hex, binary
        intStr = str( self.v )
        binStr = bin( self.v )
        hexStr = hex( self.v )
        return intStr + " " + hexStr + " " + " " + binStr

def checkBin( strToCheckB ):
    ctr = 0
    for c in strToCheckB:
        ctr = ctr + 1
        if( c != '1' and c != '0' ):
            # Not a valid binary string
            exit()
    if( ctr == 0 or ctr > 64 ):
            # More than 64 binary digits
            exit()

def checkHex( strToCheckH ):
    ctrH = 0
    for c in strToCheckH:
        ctrH = ctrH + 1
        if( c != '0' and c != '1' and c != '2' and c != '3' and c != '4' and 
          c != '5' and c != '6' and c != '7' and c != '8' and c != '9' and 
          c != 'A' and c != 'B' and c != 'C' and c != 'D' and c != 'E' and 
          c != 'F' and c != 'a' and c != 'b' and c != 'c' and c != 'd' and 
          c != 'e' and c != 'f' ):
            # Not a valid hex string
            exit()
    if( ctrH == 0 or ctrH > 16 ):
            # More than 16 hex digits
            exit()    

def checkNum( strToCheckN ):
    ctrN = 0
    for c in strToCheckN:
        ctrN = ctrN + 1
        if( c != '0' and c != '1' and c != '2' and c != '3' and c != '4' and 
          c != '5' and c != '6' and c != '7' and c != '8' and c != '9' ):
            # Not a valid numerical string/input
            exit()
    if( ctrN == 0 or ctrN > ( ( 2**64 ) - 1 ) ):
            # More than 2^( 64 ) - 1 digits
            exit()


while True:
    print( "When entering numbers, you can enter:" )
    print( "     A normal decimal integer number as big as 2^{64}-1." )
    print( "     An integer number in hex up to 16 digits, starting with 0x." )
    print( "     An integer number in binary up to 64 digits, starting with 0b." )
    print( "Enter a problem: number AND|OR|XOR|LS|RS|ANDNOT number:" )

    try:
        inputStr = raw_input(  )
    except ( EOFError ):
        exit()


    match = re.search( r'(\w+)\s+(\w+)\s+(\w+)', inputStr )
    if not match:
        # Invalid arguments
        exit()
    else:
        num1 = match.group( 1 )
        operation = match.group( 2 )
        num2 = match.group( 3 )
        numberA = None
        numberB = None

        # Check num1 format
        if( num1[ 0 ] == 'B' ): #is a binary
            checkBin( num1[ 1: ] )
            oneBInt = int( num1[ 1: ], 2 )
            numberA = Number( oneBInt )
        elif( num1[ 0:2 ] == "0x" ): #is a hex
            checkHex( num1[ 2: ] )
            oneHInt = int( num1[ 2: ], 16 )
            numberA = Number( oneHInt )
        else:
            found = re.search( r'(\d+)', num1 )
            if( found.group( 0 ) != None ):
                checkNum( num1 )
                numberA = Number( int( found.group( 1 ) ) )
            else:
                numberA = None 

        # Check num2 format
        if( num2[ 0 ] == 'B' ): #is a binary
            checkBin( num2[ 1: ] )
            twoBInt = int( num2[ 1: ], 2 )
            numberB = Number( twoBInt )
        elif( num2[ 0:2 ] == "0x" ): #is a hex
            checkHex( num2[ 2: ] )
            twoHInt = int( num2[ 2: ], 16 )
            numberB = Number( twoHInt )
        else:
            found2 = re.search( r'(\d+)', num2 )
            if( found2.group( 0 ) != None ):
                checkNum( num2 )
                numberB = Number( int( found2.group( 1 ) ) )
            else:
                numberB = None

        # Check if both number formats were valid
        if( numberA == None):
            print( "Bad format for the first number." )
            exit()
        elif( numberB == None ):
            print( "Bad format for the second number." )
            exit()

        numberC = None

        # Check for operand and calculate
        if( operation == "AND" ):
            numberC = Number( numberA.v & numberB.v )
        elif( operation == "OR" ):
            numberC = Number( numberA.v | numberB.v )
        elif( operation == "XOR" ):
            numberC = Number( numberA.v ^ numberB.v )
        elif( operation == "LS" ):
            numberC = Number( numberA.v << numberB.v )
        elif( operation == "RS" ):
            numberC = Number( numberA.v >> numberB.v )
        elif( operation == "ANDNOT" ):
            numberC = Number( numberA.v & ( ~numberB.v ) )
        else:
            print( "Bad operator." )
            exit()

    """
    Outputs
    expected results look like:

    Operation: AND
    A: 5    0x5    0b101
    B: 9    0x9    0b1001
    C: 1    0x1    0b1

      ( this example takes input:   5 AND 9 )

    """
    # output
    print "\nCompute Result:"
    print "     Operation: ", operation
    print "     A: ", numberA.toString()
    print "     B: ", numberB.toString()
    print "     C: ", numberC.toString()
