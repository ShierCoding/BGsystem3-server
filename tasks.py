from invoke import task, Context


@task
def build(ctx: Context) -> None:
    """
    Vite打包
    """

    with ctx.cd("../BGsystem3-frontend"):
        ctx.run("npm run build-only", encoding="utf-8")


@task
def start(ctx: Context) -> None:
    """
    启动服务器
    """

    from main import run
    run()


@task
def prod(ctx: Context) -> None:
    """
    启动生产服务器
    """

    from main import runProd
    runProd()


@task
def dev(ctx: Context) -> None:
    """
    启动开发服务器
    """

    from main import runDev
    runDev()


@task
def transcode(ctx: Context) -> None:
    """
    视频转码
    """

    from transcode import main
    main()
