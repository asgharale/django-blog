$i = 0
while ($i -lt 10) {
    New-Item -ItemType Directory -Name $i
    $i++
}
