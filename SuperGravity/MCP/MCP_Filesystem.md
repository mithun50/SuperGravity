# Filesystem MCP Server

**Purpose**: File system operations - read, write, manage files and directories

## Triggers
- File creation or modification needs
- Directory structure operations
- File content reading/writing
- Batch file operations
- File search and organization

## Choose When
- **For files**: Creating, reading, updating, deleting files
- **For directories**: Creating, listing, organizing folders
- **For search**: Finding files by name or pattern
- **For bulk ops**: Batch file operations

## Works Best With
- **Sequential**: Plan complex file operations
- **GitHub**: Prepare files before commits

## Security Notes
- Respects file system permissions
- Be careful with destructive operations
- Always backup before bulk changes

## Examples
```
"create a new config file" → Filesystem (file creation)
"list all TypeScript files" → Filesystem (file search)
"read package.json" → Filesystem (file reading)
"organize files into folders" → Filesystem (directory operations)
```
