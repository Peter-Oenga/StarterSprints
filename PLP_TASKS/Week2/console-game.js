(function() {
    // Game Setup
    console.clear();
    console.log("%cWelcome to the Console Quest!", "color: cyan; font-size: 20px;");
    console.log("Type `game.start()` to begin your adventure.");
  
    const game = {
      player: {
        name: "",
        level: 1,
        hp: 100,
        maxHp: 100,
        attack: 10,
        xp: 0,
        inventory: [],
        gold: 50
      },
      enemies: [
        { name: "Goblin", hp: 40, attack: 8, xp: 20 },
        { name: "Skeleton", hp: 60, attack: 12, xp: 30 },
        { name: "Dark Wizard", hp: 100, attack: 18, xp: 50 }
      ],
      items: [
        { name: "Health Potion", effect: () => { game.player.hp = Math.min(game.player.hp + 50, game.player.maxHp); console.log("You healed 50 HP."); } },
        { name: "Attack Scroll", effect: () => { game.player.attack += 5; console.log("Your attack increased by 5."); } }
      ],
      start: function() {
        game.player.name = prompt("Enter your character's name:");
        console.log(`Welcome, ${game.player.name}. Your journey begins now.`);
        game.mainMenu();
      },
      mainMenu: function() {
        console.log(`\n--- Main Menu ---`);
        console.log("1. Fight a monster");
        console.log("2. View stats");
        console.log("3. View inventory");
        console.log("4. Visit shop");
        console.log("5. Rest");
        console.log("6. Exit game");
        game.input = prompt("Choose an action (1-6):");
        switch(game.input) {
          case "1": game.fight(); break;
          case "2": game.viewStats(); break;
          case "3": game.viewInventory(); break;
          case "4": game.shop(); break;
          case "5": game.rest(); break;
          case "6": console.log("Farewell, brave adventurer."); break;
          default: console.log("Invalid input."); game.mainMenu();
        }
      },
      fight: function() {
        const enemy = {...game.enemies[Math.floor(Math.random() * game.enemies.length)]};
        console.log(`\nA wild ${enemy.name} appears!`);
        while (enemy.hp > 0 && game.player.hp > 0) {
          console.log(`\n${enemy.name}: ${enemy.hp} HP | ${game.player.name}: ${game.player.hp} HP`);
          const action = prompt("Attack (a) or Use Item (i)?");
          if (action === "a") {
            enemy.hp -= game.player.attack;
            console.log(`You strike the ${enemy.name} for ${game.player.attack} damage.`);
          } else if (action === "i") {
            if (game.player.inventory.length === 0) {
              console.log("No items to use.");
              continue;
            }
            game.viewInventory(true);
            const i = parseInt(prompt("Choose item number:")) - 1;
            if (game.player.inventory[i]) {
              game.items.find(item => item.name === game.player.inventory[i]).effect();
              game.player.inventory.splice(i, 1);
            }
            continue;
          } else {
            console.log("You hesitate...");
          }
          if (enemy.hp > 0) {
            game.player.hp -= enemy.attack;
            console.log(`The ${enemy.name} hits you for ${enemy.attack} damage.`);
          }
        }
        if (game.player.hp <= 0) {
          console.log("You have been defeated... Game Over.");
        } else {
          console.log(`You defeated the ${enemy.name}! +${enemy.xp} XP`);
          game.player.xp += enemy.xp;
          game.levelUp();
          game.mainMenu();
        }
      },
      levelUp: function() {
        const requiredXp = game.player.level * 50;
        while (game.player.xp >= requiredXp) {
          game.player.xp -= requiredXp;
          game.player.level++;
          game.player.maxHp += 20;
          game.player.attack += 5;
          game.player.hp = game.player.maxHp;
          console.log(`Level up! You are now level ${game.player.level}.`);
        }
      },
      viewStats: function() {
        console.log(`\n--- ${game.player.name}'s Stats ---`);
        console.log(`Level: ${game.player.level}`);
        console.log(`HP: ${game.player.hp}/${game.player.maxHp}`);
        console.log(`Attack: ${game.player.attack}`);
        console.log(`XP: ${game.player.xp}`);
        console.log(`Gold: ${game.player.gold}`);
        game.mainMenu();
      },
      viewInventory: function(inBattle = false) {
        console.log(`\n--- Inventory ---`);
        if (game.player.inventory.length === 0) {
          console.log("You have no items.");
        } else {
          game.player.inventory.forEach((item, i) => {
            console.log(`${i + 1}. ${item}`);
          });
        }
        if (!inBattle) game.mainMenu();
      },
      shop: function() {
        console.log("\n--- Shop ---");
        console.log("1. Buy Health Potion (10g)");
        console.log("2. Buy Attack Scroll (20g)");
        console.log("3. Exit shop");
        const choice = prompt("Choose an item to buy (1-3):");
        if (choice === "1" && game.player.gold >= 10) {
          game.player.gold -= 10;
          game.player.inventory.push("Health Potion");
          console.log("You bought a Health Potion.");
        } else if (choice === "2" && game.player.gold >= 20) {
          game.player.gold -= 20;
          game.player.inventory.push("Attack Scroll");
          console.log("You bought an Attack Scroll.");
        } else if (choice === "3") {
          game.mainMenu();
          return;
        } else {
          console.log("Not enough gold or invalid option.");
        }
        game.shop();
      },
      rest: function() {
        console.log("You rest at the inn and restore your health.");
        game.player.hp = game.player.maxHp;
        game.mainMenu();
      }
    };
  
    window.game = game;
  })();
  