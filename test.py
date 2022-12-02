from sys        import argv

def testingjenkins(desired_output):

    #print relevant test results. If at least one test failed, stop execution
    if desired_output == "'pass'":
        print(desired_output)
    else:
        print('tests did not pass')
        exit('Deployement interrupted by python.')

desired_output = "'" + str(argv[1]) + "'"

if __name__ == "__main__":

    testingjenkins(desired_output)
