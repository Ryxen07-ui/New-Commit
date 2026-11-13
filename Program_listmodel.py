class ProgramModel:
    def __init__(self, description, icon_code, id,name, popular, recommended_age, tools):
        self.icon_code = icon_code
        self.id = id
        self.description = description
        self.name = name 
        self.popular = popular
        self.recommended_age = recommended_age
        self.tools = tools 
    
    class ProgramListModel:
        def __init__(self):
            self.programlist = []
        
        def AddNewProgram (self, program):
            self.programlist.append(program)
            
            
    
DeveloperProgramInstance = ProgramModel("ALearn industry-level software development skills, build real-world projects, and prepare for a professional developer career.",
                                        "developer_program",
                                        "ee558dfd-aa55-4a71-8c3e-46dcaf0c1863", 
                                        "Professional Software Developer Program", 
                                        False,
                                        "16-45 Years", 
                                        [])
SoftwareProgramInstance = ProgramModel("Rust"
                                       ,"Dart"
                                       , "Javascript"
                                       , "Golang"
                                       , True
                                       , ""
                                       , []
                                       )

plModel = ProgramModel()

plModel.AddNewProgram(DeveloperProgramInstance)
plModel.AddNewProgram(SoftwareProgramInstance)