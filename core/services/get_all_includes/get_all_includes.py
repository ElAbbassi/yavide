class GetAllIncludes():
    def __init__(self, parser, callback = None):
        self.parser = parser
        self.callback = callback

    def __call__(self, proj_root_directory, compiler_args, args):
        contents_filename = str(args[0])
        original_filename = str(args[1])

        tunit = self.parser.parse(
            contents_filename,
            original_filename,
            compiler_args,
            proj_root_directory
        )

        if self.callback:
            self.callback(
                self.parser.get_includes(tunit),
                args
            )

