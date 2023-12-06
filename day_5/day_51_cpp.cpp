
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <cstdint> // Include the header for int64_t

#include <algorithm>
#include <cctype>

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
    
    int64_t  counter = 0;
    
    bool firstLine = true;
    std::string line;

    std::vector<HolderCoords> coordsMaps;
    coordsMaps.resize(7);
    int64_t  currentMap = -1;

    while (std::getline(inputFile, line)) {

        if (firstLine) {

            std::istringstream seedStream(line);
            int64_t  seedNumber;

            std::string stringBeforeColon;
            std::getline(seedStream, stringBeforeColon, ':');

            std::string segment;
            while (seedStream >> segment) {
                
                int64_t number = std::stoll(segment);
                seeds.push_back(number);
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
            // std::cout << "current vector" << std::endl;
            // for (int z:currentVector) {
            //     std::cout << z << ' ';
            // };
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

    std::cout << "seeds are" << std::endl;
    
    for (int64_t  seed: seeds) {
        std::cout << seed << std::endl;
    };

    for (HolderCoords hc:coordsMaps) {
        std::cout << "---------------------------------" << std::endl;
        for (Coords c:hc.coords) {
            std::cout << c.destination << ' ' << c.source << ' ' << c.length << std::endl;
        };

    };

    long long min_number = LLONG_MAX;

    for (int64_t  seed:seeds) {
        
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
    
    std::cout << "THE MIN NUMBER IS: " << min_number << std::endl;

    return 0; 
}


