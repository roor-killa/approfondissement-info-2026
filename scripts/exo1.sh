NOM="la Martinique"
echo "Bonjour depuis $NOM"

for i in 1 2 3 4 5; do
    echo "Itération $i"
done

# Condition
if [ "$1" == "bonjour" ]; then
    echo "Bonjour à toi aussi !"
else
    echo "Je ne comprends pas ce mot."
    echo $1	
fi
