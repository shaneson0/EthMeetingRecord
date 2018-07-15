contract Meeting {
    string content;

    function Meeting(string tempContent) public {
        content = tempContent;
    }

    function getContent() public view returns (string tempContent_)
    {
        tempContent_ = content;
    }
}