// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BIMPlatform {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    struct User {
        string username;
        bool registered;
    }

    struct ProjectDetails {
        string trainingData;
        string designData;
        string materialData;
        string energyData;
    }

    struct Project {
        string projectName;
        bool registered;
        ProjectDetails details;
    }

    mapping(address => User) public users;
    mapping(address => Project) public projects;

    event UserRegistered(address indexed userAddress, string username);
    event ProjectRegistered(address indexed projectAddress, string projectName, ProjectDetails details);
    event Certification(address indexed entityAddress, string entityType, bool certified);

    // User Registration
    function registerUser(string memory username) public {
        require(!users[msg.sender].registered, "User already registered");
        users[msg.sender] = User(username, true);
        emit UserRegistered(msg.sender, username);
    }

    // Project Registration
    function registerProject(
        string memory projectName,
        string memory trainingData,
        string memory designData,
        string memory materialData,
        string memory energyData
    ) public {
        require(!projects[msg.sender].registered, "Project already registered");
        projects[msg.sender] = Project(projectName, true, ProjectDetails(trainingData, designData, materialData, energyData));
        emit ProjectRegistered(msg.sender, projectName, ProjectDetails(trainingData, designData, materialData, energyData));
    }

    // Certification
    function certify(address entityAddress, string memory entityType) public onlyOwner {
        // Perform certification logic
        // For simplicity, just emit an event indicating certification
        emit Certification(entityAddress, entityType, true);
    }

    // Store Project Details
    function storeProjectDetails(
        string memory projectName,
        string memory trainingData,
        string memory designData,
        string memory materialData,
        string memory energyData
    ) public {
        require(projects[msg.sender].registered, "Project not registered");
        projects[msg.sender].details = ProjectDetails(trainingData, designData, materialData, energyData);
    }

    // Get Project Details
    function getProjectDetails() public view returns (
        string memory trainingData,
        string memory designData,
        string memory materialData,
        string memory energyData
    ) {
        require(projects[msg.sender].registered, "Project not registered");
        ProjectDetails storage details = projects[msg.sender].details;
        return (details.trainingData, details.designData, details.materialData, details.energyData);
    }
}
