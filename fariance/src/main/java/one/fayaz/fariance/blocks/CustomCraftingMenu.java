package one.fayaz.fariance.blocks;

import net.minecraft.world.entity.player.Inventory;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.inventory.CraftingMenu;
import net.minecraft.world.inventory.ContainerLevelAccess;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.state.BlockState;
import one.fayaz.fariance.ItemRegistry;

public class CustomCraftingMenu extends CraftingMenu {
    // Store ContainerLevelAccess manually
    private final ContainerLevelAccess customAccess;

    public CustomCraftingMenu(int windowId, Inventory playerInventory, ContainerLevelAccess access) {
        super(windowId, playerInventory, access);
        this.customAccess = access; // Store the access reference
    }

    @Override
    public boolean stillValid(Player player) {
        // Use the manually stored ContainerLevelAccess (customAccess) instead of access
        return this.customAccess.evaluate((level, pos) -> {
            BlockState state = level.getBlockState(pos);
            // Check if the block is a vanilla or custom crafting table
            return state.is(Blocks.CRAFTING_TABLE) || isCustomCraftingTable(state);
        }, true);
    }

    private boolean isCustomCraftingTable(BlockState state) {
        // Dynamically check for any custom crafting table block
        return ItemRegistry.GENERATED_BLOCKS.values().stream().anyMatch(block -> state.is(block.get()));
    }
}
