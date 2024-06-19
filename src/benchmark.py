import time
import click
import cProfile
import pstats
from main import vishwam_model


@click.command()
@click.argument('query')
def benchmark(query):
    """
    Benchmark the response time of the vishwam_model function.
    """
    profiler = cProfile.Profile()
    profiler.enable()

    start_time = time.time()
    result = vishwam_model(query)
    end_time = time.time()

    profiler.disable()
    response_time = end_time - start_time

    click.echo(f"Response Time: {response_time:.4f} seconds")
    click.echo(f"Result: {result}")

    # Print profiling stats
    stats = pstats.Stats(profiler)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()


if __name__ == '__main__':
    benchmark()
