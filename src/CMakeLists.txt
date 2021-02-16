set(SOURCES
        main.cpp
        Class.cpp
)

add_executable(projectname
        ${SOURCES}
)

target_include_directories(projectname PRIVATE ${PROJECT_SOURCE_DIR}/include)