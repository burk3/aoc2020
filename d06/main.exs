defmodule Splitter do
    def nl(lines), do: nl(lines, [], [])
    def nl([], [], res), do: res
    def nl([], cur, res), do: [cur | res]
    def nl(["" | ls], cur, res), do: nl(ls, [], [cur | res])
    def nl([l | ls], cur, res), do: nl(ls, [l | cur], res)

    defp reducer([], acc), do: [[] | acc]
    defp reducer(l, [curr | rest]), do: [[l | curr] | rest]
    def yanl(e) do
        Enum.reduce(e, [[]], &reducer/2)
    end
end

defmodule Customs do
    def counts(group) do
        counter = fn q, acc -> Map.update(acc, q, 1, fn x -> x + 1 end) end
        reducer = fn p, acc -> Enum.reduce(p, acc, counter) end
        Enum.reduce(group, %{}, reducer)
    end

    def info(group) do
        n = length(group)
        vs = Map.values(counts(group))
        {
            length(vs),
            Enum.count(vs, &(&1 == n))
        }
    end
end

[input | _rest] = System.argv()
lines = File.stream!(input)
res = lines
    |> Enum.map(&String.trim/1)
    |> Enum.map(&String.codepoints/1)
    |> Splitter.yanl
    |> Enum.map(&Customs.info/1)
    |> Enum.reduce({0, 0}, fn {a, b}, {sa, sb} -> {sa + a, sb + b} end)
IO.inspect(res)
