package one.fayaz.fariance.blocks.signs;

import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.SoundType;
import net.minecraft.world.level.block.WallSignBlock;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraft.world.level.block.entity.SignBlockEntity;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.state.properties.WoodType;
import net.minecraftforge.registries.RegistryObject;
import one.fayaz.fariance.ItemRegistry;

public class CustomWallSignBlock extends WallSignBlock {

    public CustomWallSignBlock(Properties properties, WoodType woodType) {
        super(woodType, properties);
    }

    @Override
    public BlockEntity newBlockEntity(BlockPos pos, BlockState state) {
        return new CustomSignBlockEntity(pos, state);  // Use the custom block entity here
    }

    // Register this block in the ItemRegistry
    public static void register() {
        RegistryObject<Block> wallSign = ItemRegistry.BLOCKS.register("custom_wall_sign",
                () -> new CustomWallSignBlock(BlockBehaviour.Properties.of()
                        .noCollission().strength(1.0F).sound(SoundType.WOOD), WoodType.OAK));
    }
}