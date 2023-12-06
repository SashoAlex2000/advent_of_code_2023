
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <cstdint> // Include the header for int64_t

#include <algorithm>
#include <cctype>

// Good exercise, but it would still take hours for the program to finish :( 

class NumberGenerator {
public:
    NumberGenerator(int start, int count) : start(start), count(count) {}

    class Iterator {
    public:
        Iterator(int current) : current(current) {}

        // Define the dereference operator to get the current value
        int operator*() const {
            return current;
        }

        // Define the pre-increment operator to move to the next value
        Iterator& operator++() {
            ++current;
            return *this;
        }

        // Define the inequality operator to check for the end of the sequence
        bool operator!=(const Iterator& other) const {
            return current != other.current;
        }

    private:
        int current;
    };

    // Define begin() and end() functions to create iterators
    Iterator begin() const {
        return Iterator(start);
    }

    Iterator end() const {
        return Iterator(start + count);
    }

private:
    int start;
    int count;
};

struct Coords {
    int64_t  destination = 0;
    int64_t  source = 0;
    int64_t  length = 0;
};

struct HolderCoords {
    std::vector<Coords> coords;
};

int main() {
    
    // std::ifstream inputFile("test_input.txt");
    std::ifstream inputFile("input_5.txt");

    
    if (!inputFile.is_open()) {
        std::cerr << "Error opening file!" << std::endl;
        return 1; 
    }

    std::vector <int64_t > seeds;
    std::vector <int64_t > testSeeds;

    std::vector<NumberGenerator> vectorOfGenerators;
    
    int64_t  counter = 0;
    
    bool firstLine = true;
    std::string line;

    std::vector<HolderCoords> coordsMaps;
    coordsMaps.resize(7);
    int64_t  currentMap = -1;

    while (std::getline(inputFile, line)) {
        std::cout << "doing a line" << std::endl;
        if (firstLine) {

            std::istringstream seedStream(line);
            int64_t  seedNumber;

            std::string stringBeforeColon;
            std::getline(seedStream, stringBeforeColon, ':');

            std::string segment;
            int newCounter = 0;
            int rangeStartHolderValue;
            while (seedStream >> segment) {
                
                int64_t number = std::stoll(segment);
                seeds.push_back(number);

                if (newCounter == 0) {
                    rangeStartHolderValue = number;
                    newCounter++;
                } else {
                    // for (int64_t k = rangeStartHolderValue; k < rangeStartHolderValue + number; k++) {
                    //     testSeeds.push_back(k);
                    // };
                    NumberGenerator currentGenerator(rangeStartHolderValue, number); 
                    vectorOfGenerators.push_back(currentGenerator);
                    newCounter = 0;
                };
            }            

            firstLine = false;
            continue;
        }

        if (line.empty()) {
            currentMap++;
            continue;
        }        

        bool containsNumbers = false;

        std::istringstream iss(line);
        int64_t  number;        

        std::vector<int64_t > currentVector;

        while (iss >> number) {
            containsNumbers = true;
            
            currentVector.push_back(number);
        };

        if (currentVector.size() > 0) {

            std::cout << std::endl;

            Coords currentCoords = {currentVector[0], currentVector[1], currentVector[2]};
            coordsMaps[currentMap].coords.push_back(currentCoords);
        };   

        if (!containsNumbers) {
            std::cout << "does NOT contain numbers" << std::endl;
        };

        std::cout << line << std::endl;
    }

    
    inputFile.close();
    std::cout << "size of the vector of iteratos: " << vectorOfGenerators.size() << std::endl;
    std::cout << "seeds are" << std::endl;

    for (int64_t  seed: seeds) {
        std::cout << seed << std::endl;
    };

    std::cout << "TEST SEEDS are" << std::endl;

    // for (int64_t  ts: testSeeds) {
    //     std::cout << ts << std::endl;
    // };

    for (HolderCoords hc:coordsMaps) {
        std::cout << "---------------------------------" << std::endl;
        for (Coords c:hc.coords) {
            std::cout << c.destination << ' ' << c.source << ' ' << c.length << std::endl;
        };

    };

    long long min_number = LLONG_MAX;

    for (const NumberGenerator& generator : vectorOfGenerators) {
        for (int64_t seed : generator) {
            
            std::cout << "--------------------" << std::endl;
            std::cout << "The seed is: " << seed << std::endl;

            for (HolderCoords hc:coordsMaps) {
                
                for (Coords c:hc.coords) {
                    // std::cout << c.destination << ' ' << c.source << ' ' << c.length << std::endl;
                    if (seed >= c.source && seed < c.source + c.length) {
                        seed = c.destination + (seed - c.source);
                        break;
                    };
                };

            };

            std::cout << "--------------------" << std::endl;
            std::cout << "Transformed seed is: " << seed << std::endl;
            if (seed < min_number) {
                std::cout << "Lower than min!" << seed << std::endl;
                min_number = seed;
            };  

        };
    } 
    std::cout << "THE MIN NUMBER IS: " << min_number << std::endl;

    return 0; 
}


